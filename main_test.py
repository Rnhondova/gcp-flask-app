import main


def test_index():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get("/")
    assert r.status_code == 200
    assert (
        "Hello World! This is a landing page to a sample project showing continuous delivery."
        in r.data.decode("utf-8")
    )
