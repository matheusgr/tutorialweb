function requestCanvas_(url) {
    const settings = getSettings()
    const token = settings['token']
    const headers = {'Authorization': 'Bearer ' + token}
    const options = {'headers': headers}
    
    var response = UrlFetchApp.fetch(url, options)
    var data = JSON.parse(response.getContentText())
  
    return {'data': data, 'link': response.getAllHeaders()['Link']}
  }