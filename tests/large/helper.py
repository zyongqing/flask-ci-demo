import os
from flask import url_for as flask_url_for
from requests.compat import urljoin


def url_for(endpoint):
    domain_name = os.getenv("WEB_DOMAIN", "web")
    return urljoin("http://{}".format(domain_name), flask_url_for(endpoint))
