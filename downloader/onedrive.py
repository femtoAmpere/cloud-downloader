# Get all links to MS OneDrive and save them to a text file.
# TODO Actually download files the links point to.
def get_onedrive(soup):
    print('Getting OneDrive links..')
    links = []
    for link in soup.findAll('a'):
        this_link = link.get('href')
        if any(linkpart in str(this_link).lower() for linkpart in ['live', 'onedrive', '1drv.ms']):
            links.append(str(this_link))
    with open('OneDrive.txt', 'a+') as file:
        for this_url in links:
            file.write(str(this_url) + '\n')
    file.close()