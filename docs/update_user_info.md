### 获取用户信息

**请求地址**:
```
    PUT/PATCH    /api/v1/user_info/[id]/
```

**请求参数**:
```
    "university":   str     大学
    "major":        str     专业
    "sleep_time":   str     睡觉时间
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