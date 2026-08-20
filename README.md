# Research Group Management API - Tiết 1

Code được viết lại theo phong cách của file tham khảo `ss23.zip`.

## Phần bắt buộc đã hoàn thành

- Khởi tạo project FastAPI.
- Cấu hình `.env`.
- Kết nối MySQL.
- Tạo `engine`, `SessionLocal`, `Base`, `get_db`.
- Model `User`.
- Model `ResearchProject`.
- Model `ResearchMember`.
- Model `ResearchTask`.
- Quan hệ giữa các model.
- Schema Base / Create / Update / Response.
- `from_attributes = True`.
- Exception 400 / 403 / 404.
- Endpoint kiểm tra API: `/health`.
- Tự tạo bảng bằng `Base.metadata.create_all()`.

## Không bao gồm

- Seed data.
- Các task không bắt buộc khác của Tiết 1.

## Cài đặt

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Sửa `DATABASE_URL` trong file `.env`.

Tạo database:

```sql
CREATE DATABASE research_management
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Chạy project:

```bash
uvicorn app.main:app --reload
```

Swagger:

`http://127.0.0.1:8000/docs`
