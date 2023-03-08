FROM public.ecr.aws/lambda/python:3.8

COPY ./requirements.txt .

RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY ./app.py ${LAMBDA_TASK_ROOT}
COPY ./helloworld ${LAMBDA_TASK_ROOT}/helloworld

CMD [ "app.handler" ]