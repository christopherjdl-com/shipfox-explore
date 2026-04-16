from app import app


def test_index_without_guest_hides_greeting_and_replaces_template_tokens():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert 'class="greeting reveal delay-3" style="display:none;"' in body
    assert "{{greeting}}" not in body
    assert "{{greeting_style}}" not in body
    assert "{{image_data_uri}}" not in body
    assert 'src="data:image/png;base64,' in body


def test_index_with_guest_renders_greeting():
    client = app.test_client()

    response = client.get("/", query_string={"guest": "Ada"})

    assert response.status_code == 200
    assert "Welcome Ada" in response.get_data(as_text=True)


def test_index_with_guest_trims_whitespace():
    client = app.test_client()

    response = client.get("/", query_string={"guest": "  Ada  "})

    assert response.status_code == 200
    assert "Welcome Ada" in response.get_data(as_text=True)


def test_index_escapes_guest_html():
    client = app.test_client()

    response = client.get("/", query_string={"guest": "<script>alert(1)</script>"})

    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert "Welcome &lt;script&gt;alert(1)&lt;/script&gt;" in body
    assert "<script>alert(1)</script>" not in body
