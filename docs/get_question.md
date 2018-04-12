### 获取问卷数据

**请求地址**:
```
    GET     /api/v1/question/
```

**请求参数**:
```
    openid    str     必填
```

**成功返回**：
```


{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "id": 3,
        "user": 1,
        "question1": 3,
        "question2": 2,
        "question3": 1,
        "question4": 1,
        "question5": 1,
        "question6": 1
    },
    "field_name": ""
}


```

**失败返回**：
```

```