# Account Book API

## Summary

| Members                          | Description                |
| -------------------------------- | -------------------------- |
| POST /users/                     | 사용자 생성                |
| POST /users/login                | 사용자 로그인              |
| POST /users/logout               | 사용자 로그아웃            |
| GET /book/{year}/{month}         | 월별 가계부 금액 내역 조회 |
| GET /book/{year}/{month}/{date}  | 일별 가계부 내역 조회      |
| POST /book/{year}/{month}/{date} | 일별 가계부 내역 생성      |
| GET /book/expenses/{expense_id}  | 가계부 세부 내역 조회      |
| PATC /book/expenses/{expense_id} | 가계부 세부 내역 수정      |
| POST /book/expenses/{expense_id} | 가계부 세부 내역 복제      |
| GET /urls?encoded={encoded_id}   | 원본 URL 조회              |
| POST /urls/                      | 단축 URL 생성              |

<br/>

## Detail

### **사용자 생성** POST /users/

- email, password 를 받아 새로운 user 를 생성합니다.
- 동시에 user 와 일대일 관계를 맺는 가계부(book) 인스턴스를 생성합니다.
- 가계부는 오로지 사용자 생성 시에 생성되며 사용자가 임의로 생성할 수 없습니다.

#### Request body

| Field    | Type   | Description       |
| -------- | ------ | ----------------- |
| email    | string | 사용자의 이메일   |
| password | string | 사용자의 비밀번호 |

#### Response

| Field | Type   | Description     |
| ----- | ------ | --------------- |
| pk    | int    | 사용자의 id     |
| email | string | 사용자의 이메일 |

<br/>

### **사용자 로그인** POST /users/login

- email, password 를 받아 jwt 토큰을 반환합니다.
- 이때의 jwt 토큰은 사용자 pk 와 토큰 만료시기(expired_at)가 암호화되어 저장됩니다.
- 이후 사용자는 요청과 함께 서버에 토큰을 전달합니다
- 토큰은 복호화되어 사용자 pk와 일치하는 사용자를 데이터베이스에서 찾아 인증권한을 부여합니다.
- 이때, 만료시기(expired_at)가 지난 경우 사용자에게 인증권한이 부여되지 않습니다.

#### Request body

| Field    | Type   | Description       |
| -------- | ------ | ----------------- |
| email    | string | 사용자의 이메일   |
| password | string | 사용자의 비밀번호 |

#### Response

| Field | Type   | Description |
| ----- | ------ | ----------- |
| token | string | 인증 토큰   |

<br/>

---

### **월별 가계부 금액 내역 조회** GET /book/{year}/{month}

- 요청한 사용자와 일대일 관계인 가계부(book) 에서 사용내역이 검색됩니다.
- 해당 월에 사용한 금액이 일별로 합산되어 반환됩니다.
- 날짜 순으로 정렬되어 날짜와 합산 금액이 각각 키와 값으로 반환됩니다.

#### URL 경로

| Directory | Type | Description |
| --------- | ---- | ----------- |
| year      | int  | 조회할 년도 |
| month     | int  | 조회할 월   |

#### Response 예시

```JSON
GET /book/2023/1

{
    "2023-01-01": 120000,
    "2023-01-02": 35000,
    "2023-01-03": 3000,
    "2023-01-04": 57000
}
```

<br/>

---

### **일별 가계부 내역 조회** GET /book/{year}/{month}/{date}

- 요청한 사용자와 일대일 관계인 가계부(book) 에서 사용내역이 검색됩니다.
- 해당 날짜에 기록된 내역이 리스트로 반환됩니다.

#### URL 경로

| Directory | Type | Description |
| --------- | ---- | ----------- |
| year      | int  | 조회할 년도 |
| month     | int  | 조회할 월   |
| date      | int  | 조회할 일   |

#### Response 예시

```JSON
GET /book/2023/1/3

[
    {
        "pk": 1,
        "date": "2023-01-03",
        "amount": 65000,
        "memo": "기름값"
    },
    {
        "pk": 2,
        "date": "2023-01-03",
        "amount": 65000,
        "memo": "과자"
    },
    {
        "pk": 3,
        "date": "2023-01-03",
        "amount": 10000,
        "memo": "선물"
    },
]
```

<br/>

### **일별 가계부 내역 생성** POST /book/{year}/{month}/{date}

- 해당 날짜를 date 필드로 갖는 내역(expense) 인스턴스가 생성됩니다.
- 요청한 사용자의 가계부(book)를 외래키로 갖습니다.

#### URL 경로

| Directory | Type | Description |
| --------- | ---- | ----------- |
| year      | int  | 조회할 년도 |
| month     | int  | 조회할 월   |
| date      | int  | 조회할 일   |

#### Response

| Field  | Type   | Description |
| ------ | ------ | ----------- |
| pk     | int    | 내역 아이디 |
| date   | string | 내역 날짜   |
| amount | int    | 내역 금액   |
| memo   | string | 내역 메모   |

<br/>

---

### **가계부 세부 내역 조회** GET /book/expenses/{expense_id}

- id를 통해 내역(expense)이 검색되어 반환됩니다.

#### URL 경로

| Directory  | Type | Description      |
| ---------- | ---- | ---------------- |
| expense_id | int  | 세부 내역 아이디 |

#### Response

| Field  | Type   | Description |
| ------ | ------ | ----------- |
| pk     | int    | 내역 아이디 |
| date   | string | 내역 날짜   |
| amount | int    | 내역 금액   |
| memo   | string | 내역 메모   |

<br/>

### **가계부 세부 내역 수정** PATCH /book/expenses/{expense_id}

- 가계부 내역을 수정할 수 있습니다.

#### Request body

| Field  | Type   | Description |
| ------ | ------ | ----------- |
| date   | string | 내역 날짜   |
| amount | int    | 내역 금액   |
| memo   | string | 내역 메모   |

#### Response

| Field  | Type   | Description |
| ------ | ------ | ----------- |
| pk     | int    | 내역 아이디 |
| date   | string | 내역 날짜   |
| amount | int    | 내역 금액   |
| memo   | string | 내역 메모   |

<br/>

### **가계부 세부 내역 복제** POST /book/expenses/{expense_id}

- 가계부 세부 내역을 복제할 수 있습니다.
- date, amount, memo가 동일한 인스턴스가 생성되고 다른 pk를 갖습니다.

#### Response

| Field  | Type   | Description |
| ------ | ------ | ----------- |
| pk     | int    | 내역 아이디 |
| date   | string | 내역 날짜   |
| amount | int    | 내역 금액   |
| memo   | string | 내역 메모   |

<br />

---

### **원본 URL 조회** GET /urls?encoded={encoded_id}

- 단축 URL에 사용된 아이디(encoded_id)가 요청 파라미터로 사용됩니다.
- encoded_id 를 복호화하여 원본 URL이 저장된 데이터베이스의 pk 값을 얻습니다.
- pk를 통해 URL 인스턴스를 검색하여 반환합니다.
- 이때, URL 인스턴스의 expired_at 필드가 만료된 경우 인스턴스를 삭제하고 원본 URL을 반환하지 않습니다.

#### Request parameters

| Parameter  | Type   | Description |
| ---------- | ------ | ----------- |
| encoded_id | string | 단축 URL    |

#### Response

| Field      | Type   | Description        |
| ---------- | ------ | ------------------ |
| id         | int    | 원본 URL 아이디    |
| expired_at | string | 단축 URL 만료 시기 |
| url        | string | 원본 URL           |

<br/>

### **단축 URL 생성** POST /urls/

- url 과 expired_at 를 필드로 갖는 URL 인스턴스를 생성합니다.
- expired_at 는 현재 시간에서 특정 시간을 더한 값으로 설정합니다.
- URL 인스턴스가 저장된 데이터베이스의 pk 값을 base62로 인코딩하여 단축 URL의 일부로 사용합니다.

#### Request body

| Field | Type   | Description     |
| ----- | ------ | --------------- |
| url   | string | 단축할 원본 URL |

#### Response

| Field | Type   | Description |
| ----- | ------ | ----------- |
| url   | string | 단축 URL    |

---
