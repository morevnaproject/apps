from urllib import request
import json

def convert(release):
    original_version = release['tag_name'].strip('v')
    version = original_version.replace('rc.', 'rc').replace('beta.', 'pre-').replace('alpha.', 'pre-pre-')
    stability = 'testing' if release['prerelease'] else 'stable'
    released = release['published_at'][0:10]
    return {'version': version, 'original-version': original_version, 'stability': stability, 'released': released}

data = request.urlopen('https://api.github.com/repos/istio/istio/releases').read().decode('utf-8')
releases = [convert(release) for release in json.loads(data) if any(str.startswith(asset['name'], 'istioctl-') for asset in release['assets'])]
