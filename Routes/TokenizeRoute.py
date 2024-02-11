from fastapi import APIRouter, HTTPException, status
from Models.InputModel import InputModel
from MLModels.TokenizeMLModel import tokenize

router = APIRouter()


@router.post("/tokenizer", tags=["Tokenizer"])
async def tokenize_text(input_data: InputModel):
    """
    Tokeniza o texto fornecido.

    Args:
        input_data (InputModel): O modelo de entrada contendo o texto a ser tokenizado.

    Returns:
        list: Uma lista de tokens (palavras) extraídos do texto fornecido.

    Raises:
        HTTPException: Se o texto fornecido estiver vazio.
    """
    try:
        if not input_data.text:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="O texto não pode ser vazio. Por favor, insira algum texto."
            )

        tokens = tokenize(input_data.text)
        return {"tokens": tokens}

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
