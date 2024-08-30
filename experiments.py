import mlflow

def calculator(a,b):
    return a+b

if __name__ == "__main__":
    with mlflow.start_run():
        a,b = 12, 54
        result = calculator(a,b)
        print(f"My result is {result}")
        params = {"var a":a, "b":b, "result":result}
        mlflow.log_params(params)