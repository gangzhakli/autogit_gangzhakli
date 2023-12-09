
from private_gpt.server.embeddings.embeddings_router import (
    EmbeddingsBody,
    EmbeddingsResponse,
)


def test_embeddings_generation(test_client: TestClient) -> None:
    body = EmbeddingsBody(input="Embed me")
    response = test_client.post("/v1/embeddings", json=body.model_dump())

    assert response.status_code == 200
    embedding_response = EmbeddingsResponse.model_validate(response.json())
    assert len(embedding_response.data) > 0
    assert len(embedding_response.data[0].embedding) > 0server:
  env_name: ${APP_ENV:prod}
  port: ${PORT:8001}

ui:
  enabled: true
  path: /

llm:
  mode: sagemaker

sagemaker:
  llm_endpoint_name: huggingface-pytorch-tgi-inference-2023-09-25-19-53-32-140
  embedding_endpoint_name: huggingface-pytorch-inference-2023-11-03-07-41-36-479server:
  env_name: ${APP_ENV:prod}
  port: ${PORT:8001}

data:
  local_data_folder: local_data/private_gpt

ui:
  enabled: true
  path: /

llm:
  mode: mock

local:
  llm_hf_repo_id: TheBloke/Mistral-7B-Instruct-v0.1-GGUF
  llm_hf_model_file: mistral-7b-instruct-v0.1.Q4_K_M.gguf
  embedding_hf_model_name: BAAI/bge-small-en-v1.5

sagemaker:
  llm_endpoint_name: huggingface-pytorch-tgi-inference-2023-09-25-19-53-32-140
  embedding_endpoint_name: huggingface-pytorch-inference-2023-11-03-07-41-36-479

openai:
  api_key: ${OPENAI_API_KEY:}server:
  env_name: ${APP_ENV:prod}
  port: ${PORT:8001}

data:
  local_data_folder: local_data/private_gpt

ui:
  enabled: true
  path: /

llm:
  mode: mock

local:
