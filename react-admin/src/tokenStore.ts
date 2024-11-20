const inMemoryTokenStore = () => {
  let inMemoryToken = null

  const getToken = () => inMemoryToken

  const setToken = token => {
    inMemoryToken = token
    return true
  }

  const removeToken = () => {
    inMemoryToken = null
    return true
  }

  return {
    getToken,
    setToken,
    removeToken,
  }
}

export default inMemoryTokenStore()
