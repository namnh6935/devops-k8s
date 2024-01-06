# How to deploy

## common

**create namespace**

```bash
$ kubectl create -f namespace.yaml
```

**deploy secrets**

```bash
$ kubectl apply -f secrets/
```

**deploy config maps**

```bash
$ kubectl apply -f configmaps/
```

## mysql

```bash
$ kubectl apply -f mysql/
```


## app

```bash
$ kubectl apply -f nodejs-app/
$ kubectl apply -f dotnet-app/
```
