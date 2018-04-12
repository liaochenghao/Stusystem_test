### 创建用户

**请求地址**:
```
    POST    /api/v1/user_info/
```

**请求参数**:
```
    CODE      微信验证的CODE值  必填
```

**成功返回**：
```


{
    "code": 0,
    "msg": "请求成功",
    "data": [
        {
            "id": 1,
            "university": "加州大学",
            "major": "建筑学",
            "sleep_time": "23:30:00",
            "nickname": "测试",
            "head_img": "http://www.chinasummer.org/assets/images/zaixian.png"
        }
    ],
    "field_name": ""
}


```

**失败返回**：
```

```