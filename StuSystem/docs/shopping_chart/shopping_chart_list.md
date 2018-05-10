### 用户购物车列表

**请求地址**:
```
    GET     /order/shopping_chart/
```

**请求参数**:
```
    无
```

**成功返回**：
```
{
    "code": 0,
    "msg": "请求成功",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "project": {    项目信息
                    "id": 10,
                    "campus": {     项目校区信息
                        "id": 18,
                        "name": "武汉校区",
                        "info": "针对国际业务",
                        "create_time": "2017-11-14T09:14:48Z",
                        "network_course": false
                    },
                    "name": "冬季课程",
                    "start_date": "2017-12-25",
                    "end_date": "2018-01-12",
                    "address": "武汉市",
                    "info": "2017年12月25日至2018年1月12日（3周课程）",
                    "create_time": "2017-11-14T10:06:32Z",
                    "apply_fee": 2000.0,
                    "course_num": 4,
                    "project_course_fee": [
                        {
                            "id": 65,
                            "course_number": 1,
                            "course_fee": 23120.0,
                            "course_info": "1门"
                        },
                        {
                            "id": 66,
                            "course_number": 2,
                            "course_fee": 23120.0,
                            "course_info": "2门"
                        },
                        {
                            "id": 67,
                            "course_number": 3,
                            "course_fee": 28120.0,
                            "course_info": "3门"
                        }
                    ]
                },
                "course_num": 3,
                "course_fee": 28120.0,
                "create_time": "2017-11-15T07:06:14Z",
                "stu_score_detail": { 学生成绩单寄送详情
                    "id": 10,
                    "user": 2,
                    "department": "材料科学与工程学院",
                    "phone": "18608146540",
                    "country": "美国",
                    "post_code": "021878768687",
                    "address": "纽约市布鲁克林区布鲁克林大道58号"
                }
            }
        ]
    },
    "field_name": ""
}
```

**失败返回**：
```

```