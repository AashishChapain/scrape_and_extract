
data = [
    {
        'company_name': 'Woebot Health',
        'url': 'http://www.woebothealth.com/',
        'segment': 'Mental Health'
    },
    {
        'company_name': 'NeuroFlow',
        'url': 'http://www.neuroflow.com/',
        'segment': 'Mental Health'
    },
    {
        'company_name': 'Sonnest Health',
        'url': 'http://www.sonnest.com/',
        'segment': 'Medical Imaging/Cardiovascular'
    },
    # {
    #     'company_name': 'MERU HEALTH',
    #     'url': 'http://www.meruhealth.com/',
    #     'segment': 'Mental Health'
    # },
    {
        'company_name': 'Unmind',
        'url': 'http://www.unmind.com/',
        'segment': 'Mental Health'
    }
    ,
    {
        'company_name': 'Ieso Digital Health',
        'url': 'http://www.iesohealth.com/',
        'segment': 'Mental Health'
    },
    # {
    #     'company_name': 'Click Therapeutics',
    #     'url': 'http://www.clicktherapeutics.com/',
    #     'segment': 'Mental Health'
    # },
    {
        'company_name': 'Alma',
        'url': 'http://www.helloalma.com/',
        'segment': 'Mental Health'
    },
    # {
    #     'company_name': 'On Demand Counseling',
    #     'url': 'http://www.ondemandoccupationalmedicine.com/',
    #     'segment': 'Psychology Companies'
    # },
    {
        'company_name': 'International Association of Applied Psychology',
        'url': 'http://www.iaapsy.org/',
        'segment': 'Psychology Organizations'
    },
    # {
    #     'company_name': 'Vox Nutrition',
    #     'url': 'http://www.voxnutrition.com/',
    #     'segment': 'Nutraceutical Companies'
    # },
    # {
    #     'company_name': 'Elmed Life Sciences Pvt',
    #     'url': 'http://www.elmedlifesciences.com/',
    #     'segment': 'Nutraceutical Companies'
    # },
    {
        'company_name': 'Divi’s Nutraceutical',
        'url': 'http://www.divisnutra.com/',
        'segment': 'Nutraceutical Companies'
    },
]


def get_data():
    urls = [d['url'] for d in data]
    company_names = [d['company_name'] for d in data]
    segments = [d['segment'] for d in data]

    return urls, company_names, segments