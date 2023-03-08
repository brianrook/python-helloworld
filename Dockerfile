FROM public.ecr.aws/lambda/python:3.10

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY ./logging.conf ${LAMBDA_TASK_ROOT}
COPY ./aws.py ${LAMBDA_TASK_ROOT}
COPY ./app ${LAMBDA_TASK_ROOT}

CMD [ "aws.handler" ]