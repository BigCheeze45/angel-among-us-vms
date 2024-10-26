/* eslint-disable @typescript-eslint/no-explicit-any */
import {
  RaRecord,
  HttpError,
  Identifier,
  fetchUtils,
  SortPayload,
  GetOneParams,
  GetOneResult,
  UpdateParams,
  DataProvider,
  UpdateResult,
  CreateParams,
  CreateResult,
  DeleteParams,
  DeleteResult,
  GetListParams,
  GetListResult,
  GetManyParams,
  GetManyResult,
  FilterPayload,
  DeleteManyParams,
  DeleteManyResult,
  UpdateManyParams,
  UpdateManyResult,
  PaginationPayload,
  QueryFunctionContext,
  GetManyReferenceParams,
  GetManyReferenceResult,
} from "react-admin"

import {stringify} from "query-string"
import {ENDPOINTS, HttpMethod, API_BASE_URL} from "./constants"

export const getPaginationQuery = (pagination: PaginationPayload) => {
  return {
    page: pagination.page,
    page_size: pagination.perPage,
  }
}

export const getFilterQuery = (filter: FilterPayload) => {
  const {q: search, ...otherSearchParams} = filter
  return {
    ...otherSearchParams,
    search,
  }
}

export const getOrderingQuery = (sort: SortPayload) => {
  const {field, order} = sort
  return {
    ordering: `${order === "ASC" ? "" : "-"}${field}`,
  }
}

export const fetchJson = (url: string, options: fetchUtils.Options = {}) => {
  // make any additional changes before sending the request
  return fetchUtils.fetchJson(url, options)
}

/**
 * Generate API url for the given resource and query parameters
 * @param apiRoot root api url
 * @param resource api resource/endpoint
 * @param queryParams additional parameters to be included as URL query parameters
 * @returns complete url
 */
function generateUrl(apiRoot: string, resource: string, queryParams?): string {
  // Ensure apiRoot doesn't end with a slash and resource doesn't start
  // with a slash
  const cleanApiRoot = apiRoot.replace(/\/$/, "")
  const cleanResource = resource.replace(/^\//, "")

  // Combine apiRoot and resource
  let url = `${cleanApiRoot}/${cleanResource}/`

  // apply any query parameters, if available
  if (queryParams) url += `?${stringify(queryParams)}`

  return url
}

/**
 * Fetch a single object from the API
 * @param apiUrl root api URL
 * @param resource api resource/endpoint
 * @param params request body
 * @returns the resource/object
 */
async function fetchOne<RecordType extends RaRecord = any>(
  apiUrl: string,
  resource: string,
  params: GetOneParams<RecordType>,
): Promise<GetOneResult<RecordType>> {
  const url = generateUrl(apiUrl, `${resource}/${params.id}`)
  const {json} = await fetchJson(url, {method: HttpMethod.GET})
  return {data: json}
}

/**
 * Update a single resource on the API
 * @param apiUrl root api URL
 * @param resource api resource/endpoint
 * @param params request body
 * @returns the updated resource
 */
async function updateOne<RecordType extends RaRecord = any>(
  apiUrl: string,
  resource: string,
  params: UpdateParams<RecordType>,
): Promise<UpdateResult<RecordType>> {
  const url = generateUrl(apiUrl, `${resource}/${params.id}`)
  const {json} = await fetchJson(url, {
    body: JSON.stringify(params.data),
    method: HttpMethod.PATCH,
  })
  return {data: json}
}

/**
 * Delete a single resource on the API
 * @param apiUrl root api URL
 * @param resource api resource/endpoint
 * @param params request body
 * @returns the deleted resource
 */
async function deleteOne<RecordType extends RaRecord = any>(
  apiUrl: string,
  resource: string,
  params: DeleteParams<RecordType>,
): Promise<DeleteResult<RecordType>> {
  const url = generateUrl(apiUrl, `${resource}/${params.id}`)
  const {json} = await fetchJson(url, {method: HttpMethod.DELETE})
  return {data: json}
}

/**
 * React-Admin adapter to talk to DRF backend. Whenever react-admin needs to
 * communicate with your APIs, it does it through an object called the
 * dataProvider. The dataProvider exposes a predefined interface that allows
 * react-admin to query any API in a normalized way.
 *
 * https://marmelab.com/react-admin/DataProviders.html
 */
export default (apiUrl: string = API_BASE_URL): DataProvider => ({
  getList: async function <RecordType extends RaRecord = any>(
    resource: string,
    params: GetListParams & QueryFunctionContext,
  ): Promise<GetListResult<RecordType>> {
    const query = {
      ...getFilterQuery(params.filter),
      ...getPaginationQuery(params.pagination),
      ...getOrderingQuery(params.sort),
    }

    const url = generateUrl(apiUrl, resource, query)
    const {json} = await fetchJson(url, {method: HttpMethod.GET})

    return {data: json.results, total: json.count}
  },
  getOne: async function <RecordType extends RaRecord = any>(
    resource: string,
    params: GetOneParams<RecordType> & QueryFunctionContext,
  ): Promise<GetOneResult<RecordType>> {
    return await fetchOne(apiUrl, resource, params)
  },
  getMany: async function <RecordType extends RaRecord = any>(
    resource: string,
    params: GetManyParams<RecordType> & QueryFunctionContext,
  ): Promise<GetManyResult<RecordType>> {
    const manyPromises = params.ids.map(id => fetchOne(apiUrl, resource, {id}))
    const results = await Promise.all(manyPromises)
    const data = results.map(json => json.data)
    return {data}
  },
  getManyReference: async function <RecordType extends RaRecord = any>(
    resource: string,
    params: GetManyReferenceParams & QueryFunctionContext,
  ): Promise<GetManyReferenceResult<RecordType>> {
    const query = {
      ...getFilterQuery(params.filter),
      ...getPaginationQuery(params.pagination),
      ...getOrderingQuery(params.sort),
      [params.target]: params.id,
    }
    const url = generateUrl(apiUrl, resource, query)
    const {json} = await fetchJson(url, {method: HttpMethod.GET})
    // TODO: include pagination info
    return {data: json.results, total: json.count}
  },
  update: async function <RecordType extends RaRecord = any>(
    resource: string,
    params: UpdateParams,
  ): Promise<UpdateResult<RecordType>> {
    return await updateOne(apiUrl, resource, params)
  },
  updateMany: async function <RecordType extends RaRecord = any>(
    resource: string,
    params: UpdateManyParams,
  ): Promise<UpdateManyResult<RecordType>> {
    const manyPromises = params.ids.map(id => updateOne(apiUrl, resource, {id, data: params.data}))
    const results = await Promise.all(manyPromises)
    const data = results.map(json => json.data)
    return {data}
  },
  create: async function <
    RecordType extends Omit<RaRecord, "id"> = any,
    ResultRecordType extends RaRecord = RecordType & {id: Identifier},
  >(resource: string, params: CreateParams): Promise<CreateResult<ResultRecordType>> {
    const url = generateUrl(apiUrl, resource)
    const {json} = await fetchJson(url, {
      body: JSON.stringify(params.data),
      method: HttpMethod.POST,
    })
    return {data: json}
  },
  delete: async function <RecordType extends RaRecord = any>(
    resource: string,
    params: DeleteParams<RecordType>,
  ): Promise<DeleteResult<RecordType>> {
    return await deleteOne(apiUrl, resource, params)
  },
  deleteMany: async function <RecordType extends RaRecord = any>(
    resource: string,
    params: DeleteManyParams<RecordType>,
  ): Promise<DeleteManyResult<RecordType>> {
    const manyPromises = params.ids.map(id => deleteOne(apiUrl, resource, {id}))
    const results = await Promise.all(manyPromises)
    const data = results.map(json => json)
    return {data}
  },
  export: async function (resource: string, params: GetListParams & GetManyParams & QueryFunctionContext) {
    const query = {
      ...getFilterQuery(params.filter),
      ...getOrderingQuery(params.sort),
    }
    const export_url = `${resource}/${ENDPOINTS.EXPORT}`
    const url = generateUrl(apiUrl, export_url, query)

    const response = await fetch(url, {
      method: HttpMethod.POST,
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({format: params.meta?.format, ids: params?.ids}),
    })

    if (response.status < 200 || response.status >= 300) {
      const json = await response.json()
      throw new HttpError((json && json.detail) || response.statusText, response.status, json)
    }

    return await response.blob()
  },
})
