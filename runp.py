from library import create_app

app = create_app(config='')
app.run(debug=False)
