import json


class TestSiteVerification:
    def test_no_config(self, client):
        response = client.post('/layout/_site_verification', content_type='application/json', data=json.dumps({}))

        assert response.status_code == 200
        assert response.get_data(as_text=True).strip() == ''

    def test_with_config(self, client):
        response = client.post(
            '/layout/_site_verification',
            content_type='application/json',
            data=json.dumps({'params': {'config': {'GOOGLE_SITE_VERIFICATION': 'i-own-this'}}}),
        )

        assert response.status_code == 200
        assert response.get_data(as_text=True).strip() == '<meta name="google-site-verification" content="i-own-this">'


class TestCustomDimensions:
    def test_no_config(self, client):
        response = client.post('/layout/_custom_dimensions', content_type='application/json', data=json.dumps({}))

        assert response.status_code == 200
        assert response.get_data(as_text=True).strip() == ''

    def test_current_user_with_role(self, client):
        response = client.post(
            '/layout/_custom_dimensions',
            content_type='application/json',
            data=json.dumps({'params': {'current_user': {'role': 'staff'}}}),
        )

        assert response.status_code == 200
        assert (
            response.get_data(as_text=True).strip()
            == '<meta name="ga_customDimension" data-id="10" data-value="staff">'
        )

    def test_current_user_with_supplier_organisation_size(self, client):
        response = client.post(
            '/layout/_custom_dimensions',
            content_type='application/json',
            data=json.dumps({'params': {'current_user': {'supplier_organisation_size': '2019'}}}),
        )

        assert response.status_code == 200
        assert (
            response.get_data(as_text=True).strip() == '<meta name="ga_customDimension" data-id="11" data-value="2019">'
        )

    def test_one_custom_dimensions(self, client):
        response = client.post(
            '/layout/_custom_dimensions',
            content_type='application/json',
            data=json.dumps({'params': {'custom_dimensions': [{'data_id': 1, 'data_value': 'screen-size'}]}}),
        )

        assert response.status_code == 200
        assert (
            response.get_data(as_text=True).strip()
            == '<meta name="ga_customDimension" data-id="1" data-value="screen-size">'
        )

    def test_multiple_custom_dimensions(self, client):
        response = client.post(
            '/layout/_custom_dimensions',
            content_type='application/json',
            data=json.dumps(
                {
                    'params': {
                        'custom_dimensions': [
                            {'data_id': 1, 'data_value': 'screen-size'},
                            {'data_id': 2, 'data_value': 'device'},
                        ]
                    }
                }
            ),
        )
        assert response.status_code == 200
        assert (
            response.get_data(as_text=True).strip().replace('\n', '')
            == '<meta name="ga_customDimension" data-id="1" data-value="screen-size">  '
            '<meta name="ga_customDimension" data-id="2" data-value="device">'
        )
