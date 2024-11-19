(tutorial)=
# Making Changes
Modifying the code is fairly simple once you know where the different parts
live. For that, checkout the [overview page](overview.rst). A basic understanding
of the 3 core technologies along with some familiarity with Python and
TypeScript is enough.

This tutorial is divided into two parts. The first focuses on bringing
in new data from iShelters. The second part demonstrates how to create
filters using Django filters. By the end, you will understand:

* how to change (or create) models
* update the `sync` command to pull data from iShelters
* make the new data available to the frontend
* update frontend components/views to show the new data
* make the new data filterable

As a simple but illustrative example, we will be bringing over
the `personHouseInspectionStatusId` field from the `person` table.
In the VMS, we will create this as a boolean column where 471 is true
and everything else false.

## Part I: Bringing in the data
### 1: Update the model
The first thing we need to do is make sure our application, and more importantly,
the database is setup to accept this new field. We will store this field
inside of our Volunteer model instead of creating a new one.
```python
class Volunteer(models.Model):
    # All the other columns are not shown here for clarity
    housing_inspection_status = models.BooleanField(null=True)
```
### 2: Generate migration files
After modifying the model, we need to generate migration files using `makemigrations`,
which is responsible for creating new migrations based on the changes
you have made to your models. This will output a new migration file in `app/migrations`.

We can use the make [target](./admin/make.md):

`make makemigrations`
### 3: Apply the migration
Now we need to apply the migration files to the database for the new column
to be added. Again, we can use the make target:

`make migrate`
### 4: Update ETL
These 3 steps have configure our application to accept the new field. Next we
need to update the ETL to bring over the data.

Since we're bring this new field into the Volunteer model, we need to update the ETL
query that pulls from the `person` table.
```python
# In app/management/commands/sync.py
# Truncated statement for clarity
base_volunteer_query =
    """
    SELECT
        -- Use column alias to match Django model field names
        IF(personHouseInspectionStatusId = 471, 1, 0) AS housing_inspection_status
    FROM
        person p
    """
```
Run `make sync` to pull this data and update the VMS field.
### 5: Make the new data available to the frontend
In the case of Volunteers most fields are returned automatically so there is
nothing to do here. However, to change what is returned to the frontend,
look at the corresponding [serializer](https://www.django-rest-framework.org/api-guide/serializers/) for that model.

## Part II: Update frontend to display new field
Since the new field is now available to the frontend, we can display it anywhere
using [React-Admin fields](https://marmelab.com/react-admin/Fields.html).

We're going to show it in the table of Volunteers
```jsx
// Shorten for clarity
// react-admin/src/views/volunteers/VolunteersList.tsx
export const VolunteersList = () => {
  return (
    <List>
      <DatagridConfigurable>
        <BooleanField source="housing_inspection_status" label="House Inspected" />
      </DatagridConfigurable>
    </List>
  )
}
```
## Part III: Filtering the data
One of the killer feature of the VMS is the filtering and query building
that's available. This part of the tutorial will go over setting that
up.

### 1: Update view filters
Since `housing_inspection_status` is a simple yes/no toggle we just need to add it
to the `fields` attribute of our filter class. This will perform an exact match
query (i.e. `?housing_inspection_status=true`).

Checkout [DRF filtering library](https://github.com/philipn/django-rest-framework-filters/blob/v0.10.2/README.rst) for more information and examples.

```python
# In app/views/VolunteerViewSet.py
class VolunteerFilters(filters.FilterSet):
    class Meta:
        model = Volunteer
        fields = [..., "housing_inspection_status"]
```

### 2: Add filters to frontend
```jsx
// Shorten for clarity
// react-admin/src/views/volunteers/VolunteersFilterSidebar.tsx
export const VolunteerFilterSidebar = () => {
  return (
    <Card>
      <CardContent>
        <FilterList
          label="Home inspected"
          icon={<StarBorderIcon />}
        >
          <FilterListItem
            label="Yes"
            value={{housing_inspection_status: true}}
          />
          <FilterListItem
            label="No"
            value={{housing_inspection_status: false}}
          />
        </FilterList>
        </CardContent>
    </Card>
  )
}
```
