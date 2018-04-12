### 提交问卷

**请求地址**:
```
    POST    /api/v1/question/
```

**请求参数**:
```
    user        int   用户id
    
    question1   str   第一题
    question2   str   第二题
    question3   str   第三题
    question4   str   第四题
    question5   str   第五题
    question6   str   第六题
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