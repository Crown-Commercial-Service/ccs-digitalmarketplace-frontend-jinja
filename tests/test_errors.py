import json

from lxml import html


class Test400:
    def test_400_no_error_message(self, client):
        response = client.post('/error/400', content_type='application/json', data=json.dumps({}))

        assert response.status_code == 200

        doc = html.fromstring(response.get_data(as_text=True))

        assert doc.xpath('//title')[0].text_content().strip() == 'Bad request - Digital Marketplace'
        assert doc.xpath('//h1')[0].text_content().strip() == 'Sorry, there was a problem with your request'
        assert doc.xpath('//main/p')[0].text_content().strip() == 'Please do not attempt the same request again.'

    def test_400_with_error_message(self, client):
        response = client.post(
            '/error/400',
            content_type='application/json',
            data=json.dumps({'params': {'error_message': 'This is a test error message for 400'}}),
        )

        assert response.status_code == 200

        doc = html.fromstring(response.get_data(as_text=True))

        assert doc.xpath('//title')[0].text_content().strip() == 'Bad request - Digital Marketplace'
        assert doc.xpath('//h1')[0].text_content().strip() == 'Sorry, there was a problem with your request'
        assert doc.xpath('//main/p')[0].text_content().strip() == 'This is a test error message for 400'


class Test403:
    def test_403(self, client):
        response = client.post('/error/403', content_type='application/json', data=json.dumps({}))

        assert response.status_code == 200

        # print(response.get_data(as_text=True))
        doc = html.fromstring(response.get_data(as_text=True))

        assert doc.xpath('//title')[0].text_content().strip() == 'Access denied - 403 – Digital Marketplace'

        breadcrumbs = doc.xpath('//main/nav/ol/li')

        assert (
            breadcrumbs[0].xpath('./a[@class="govuk-breadcrumbs__link"][@href="/"]')[0].text_content() == 'Admin home'
        )
        assert breadcrumbs[1].text_content() == 'Access denied'

        assert doc.xpath('//h1')[0].text_content().strip() == 'You don’t have permission to perform this action'

        body = doc.xpath('//main/p')[0]

        assert (
            body.xpath('./a')[0].get('href')
            == 'mailto:enquiries@digitalmarketplace.service.gov.uk?subject=Digital%20Marketplace%20feedback'
        )
        assert (
            body.xpath('./a')[0].get('title') == 'Please send feedback to enquiries@digitalmarketplace.service.gov.uk'
        )

        assert (
            body.text_content().strip()
            == 'Email enquiries@digitalmarketplace.service.gov.uk if you need to access this content.'
        )


class Test404:
    def test_404(self, client):
        response = client.post('/error/404', content_type='application/json', data=json.dumps({}))

        assert response.status_code == 200

        # print(response.get_data(as_text=True))
        doc = html.fromstring(response.get_data(as_text=True))

        assert doc.xpath('//title')[0].text_content().strip() == 'Page could not be found - Digital Marketplace'
        assert doc.xpath('//h1')[0].text_content().strip() == 'Page could not be found'

        body = doc.xpath('//main/p')

        assert (
            body[0].text_content().strip()
            == 'Check you’ve entered the correct web address or start again on the Digital Marketplace homepage.'
        )

        assert (
            body[1].xpath('./a')[0].get('href')
            == 'mailto:cloud_digital@gca.gov.uk?subject=Digital%20Marketplace%20feedback'
        )
        assert body[1].xpath('./a')[0].get('title') == 'Please send feedback to cloud_digital@gca.gov.uk'

        assert (
            body[1].text_content().strip()
            == 'If you can’t find what you’re looking for, contact us at cloud_digital@gca.gov.uk'
        )


class Test410:
    def test_410(self, client):
        response = client.post('/error/410', content_type='application/json', data=json.dumps({}))

        assert response.status_code == 200

        # print(response.get_data(as_text=True))
        doc = html.fromstring(response.get_data(as_text=True))

        assert doc.xpath('//title')[0].text_content().strip() == 'Service no longer available - Digital Marketplace'
        assert doc.xpath('//h1')[0].text_content().strip() == 'Page no longer available'

        body = doc.xpath('//main/p')

        assert (
            body[0].text_content().strip()
            == 'The page you requested is no longer available on the Digital Marketplace.'
        )

        assert (
            body[1].xpath('./a')[0].get('href')
            == 'mailto:cloud_digital@gca.gov.uk?subject=Digital%20Marketplace%20page%20gone'
        )
        assert body[1].xpath('./a')[0].get('title') == 'Please send feedback to cloud_digital@gca.gov.uk'

        assert (
            body[1].text_content().strip()
            == "If you can't find what you're looking for, email cloud_digital@gca.gov.uk"
        )


class Test500:
    def test_500_no_error_message(self, client):
        response = client.post('/error/500', content_type='application/json', data=json.dumps({}))

        assert response.status_code == 200

        doc = html.fromstring(response.get_data(as_text=True))

        assert (
            doc.xpath('//title')[0].text_content().strip()
            == 'Sorry, we’re experiencing technical difficulties - Digital Marketplace'
        )
        assert doc.xpath('//h1')[0].text_content().strip() == 'Sorry, we’re experiencing technical difficulties'
        assert doc.xpath('//main/p')[0].text_content().strip() == 'Try again later.'

    def test_400_with_error_message(self, client):
        response = client.post(
            '/error/500',
            content_type='application/json',
            data=json.dumps({'params': {'error_message': 'This is a test error message for 500'}}),
        )

        assert response.status_code == 200

        doc = html.fromstring(response.get_data(as_text=True))

        assert (
            doc.xpath('//title')[0].text_content().strip()
            == 'Sorry, we’re experiencing technical difficulties - Digital Marketplace'
        )
        assert doc.xpath('//h1')[0].text_content().strip() == 'Sorry, we’re experiencing technical difficulties'
        assert doc.xpath('//main/p')[0].text_content().strip() == 'This is a test error message for 500'
