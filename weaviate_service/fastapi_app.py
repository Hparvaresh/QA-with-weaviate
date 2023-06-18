from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import get_qa


fastapi_application = FastAPI()
fastapi_application.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)

fastapi_application.include_router(get_qa.router)
