from library.app import create_app

app = create_app(config='')
app.run(debug=False)
