FROM public.ecr.aws/lambda/python:3.8

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY app.py ${LAMBDA_TASK_ROOT}
ADD ./helloworld/ ${LAMBDA_TASK_ROOT}

CMD [ "app.handler" ]