import uvicorn


if __name__ == '__main__':

	uvicorn.run(
		"fastapi_app:fastapi_application",
		host="0.0.0.0",
		port=8085
	)
