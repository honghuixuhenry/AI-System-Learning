from rpc_models import (
    EmbeddingRequest,
    EmbeddingResponse
)


class EmbeddingService:

    def generate_embedding(
        self,
        request: EmbeddingRequest
    ) -> EmbeddingResponse:

        values = [
            float(len(request.text)),
            1.0,
            0.5
        ]

        return EmbeddingResponse(
            dimensions=len(values),
            values=values
        )