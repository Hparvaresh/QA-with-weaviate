import json
from pydantic import BaseModel
from fastapi import APIRouter, Response
from qa_module.weaviate_manager import WeaviateManager


class GetQA(BaseModel):

    question: str


router = APIRouter()
weaviate_man = WeaviateManager()


@router.post('/qa_answering')
def qa_answering(request: GetQA):

    answer, error = weaviate_man.question(ask_question=request.question)

    if error:
        response_content, response_status = error, 501

    else:
        response_content, response_status = answer, 200

    return Response(
        content=json.dumps(response_content),
        status_code=response_status,
        media_type="application/json")
