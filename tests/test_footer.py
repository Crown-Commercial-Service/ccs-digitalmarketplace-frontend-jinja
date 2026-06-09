import json

FOOTER_FIXTURES_PATH = (
    'node_modules/digitalmarketplace-frontend/dist/digitalmarketplace/components/footer/fixtures.json'
)


def get_footer_example(name):
    with open(FOOTER_FIXTURES_PATH) as file:
        fixtures = json.load(file)

    for fixture in fixtures['fixtures']:
        if fixture['name'] == name:
            return fixture.get('options', {})

    raise KeyError(name)


def render_footer(client, params=None):
    response = client.post(
        '/component/footer',
        content_type='application/json',
        data=json.dumps({'macro_name': 'Footer', 'params': params or {}}),
    )

    assert response.status_code == 200
    return response.get_data(as_text=True)


def render_footer_with_context(client, params=None, context=None):
    response = client.post(
        '/component/footer/with-context',
        content_type='application/json',
        data=json.dumps({'macro_name': 'Footer', 'params': params or {}, 'context': context or {}}),
    )

    assert response.status_code == 200
    return response.get_data(as_text=True)


class TestFooterSupplierLinks:
    def test_does_not_render_supplier_links_by_default(self, client):
        html = render_footer(client, get_footer_example('default'))

        assert 'G-Cloud supplier A to Z' not in html
        assert 'G-Cloud 14 supplier A to Z' not in html
        assert 'G-Cloud 15 supplier A to Z' not in html
        assert 'Digital Outcomes and Specialists supplier A to Z' not in html

    def test_renders_g_cloud_14_supplier_link_when_g_cloud_14_is_live(self, client):
        html = render_footer(client, get_footer_example('with G-Cloud 14 supplier A to Z link'))

        assert 'G-Cloud 14 supplier A to Z' in html
        assert '/g-cloud-14/suppliers' in html
        assert 'G-Cloud 15 supplier A to Z' not in html
        assert 'Digital Outcomes and Specialists supplier A to Z' not in html

    def test_renders_g_cloud_15_supplier_link_when_g_cloud_15_is_live(self, client):
        html = render_footer(client, get_footer_example('with G-Cloud 15 supplier A to Z link'))

        assert 'G-Cloud 15 supplier A to Z' in html
        assert '/g-cloud-15/suppliers' in html
        assert 'G-Cloud 14 supplier A to Z' not in html
        assert 'Digital Outcomes and Specialists supplier A to Z' not in html

    def test_renders_g_cloud_14_and_15_supplier_links_when_both_are_live(self, client):
        html = render_footer(client, get_footer_example('with G-Cloud 14 and 15 supplier A to Z links'))

        assert 'G-Cloud 14 supplier A to Z' in html
        assert '/g-cloud-14/suppliers' in html
        assert 'G-Cloud 15 supplier A to Z' in html
        assert '/g-cloud-15/suppliers' in html
        assert 'Digital Outcomes and Specialists supplier A to Z' not in html

    def test_renders_dos_supplier_link_when_dos_is_live(self, client):
        html = render_footer(client, get_footer_example('with Digital Outcomes and Specialists supplier A to Z link'))

        assert 'Digital Outcomes and Specialists supplier A to Z' in html
        assert '/digital-outcomes-and-specialists/suppliers' in html
        assert 'G-Cloud 14 supplier A to Z' not in html
        assert 'G-Cloud 15 supplier A to Z' not in html

    def test_renders_supplier_links_for_each_live_framework(self, client):
        html = render_footer(
            client, get_footer_example('with G-Cloud and Digital Outcomes and Specialists supplier A to Z links')
        )

        assert 'G-Cloud 14 supplier A to Z' in html
        assert '/g-cloud-14/suppliers' in html
        assert 'G-Cloud 15 supplier A to Z' in html
        assert '/g-cloud-15/suppliers' in html
        assert 'Digital Outcomes and Specialists supplier A to Z' in html
        assert '/digital-outcomes-and-specialists/suppliers' in html


class TestFooterLiveFrameworksListContext:
    def test_renders_supplier_links_from_live_frameworks_list_context(self, client):
        html = render_footer_with_context(
            client,
            context={'live_frameworks_list': [{'slug': 'g-cloud-14', 'name': 'G-Cloud 14'}]},
        )

        assert 'G-Cloud 14 supplier A to Z' in html
        assert '/g-cloud-14/suppliers' in html

    def test_params_live_frameworks_take_precedence_over_context(self, client):
        html = render_footer_with_context(
            client,
            params={'live_frameworks': [{'slug': 'g-cloud-15', 'name': 'G-Cloud 15'}]},
            context={'live_frameworks_list': [{'slug': 'g-cloud-14', 'name': 'G-Cloud 14'}]},
        )

        assert 'G-Cloud 15 supplier A to Z' in html
        assert '/g-cloud-15/suppliers' in html
        assert 'G-Cloud 14 supplier A to Z' not in html
