def get_api_key(file_path):
    with open(file_path, 'r') as f:
        return f.read().rstrip()
        
computer_user = 'soichi'
key = get_api_key('/Users/' + computer_user + '/.plotly/api_key')
py.tools.set_credentials_file(username='soujiro0725', api_key=key)

# may need to regenerate API key
data = [py.graph_objs.Scatter( x=df.Date, y=df.Close )]
py.plotly.iplot(data)