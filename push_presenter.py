import config
import pbclient


pbclient.set('endpoint', config.ENDPOINT)
pbclient.set('api_key', config.API_KEY)


def push_presenter():
    html = open('presenter.html').read()

    app = pbclient.find_app(short_name=config.APP)[0]

    app.info['task_presenter'] = html
    app.info['sched'] = 'default'
    pbclient.update_app(app)


if __name__ == '__main__':
    push_presenter()
