import function


function.day_limit()
function.initialize()


UA_LIST = function.generate_ua()

browser, page, p = function.open_stealth(UA_LIST,function.setting['path'])

function.login(page)

try:
    while True:
        if function.setting['li'] == 'following':
            function.navigate_to_following(page)
        elif function.setting['li'] == 'followers':
            function.navigate_to_followers(page)
        elif function.setting['li'] == 'custom':
            function.share_custom(page)
        elif function.setting['li'] == 'party':
            function.self_to_party(page)
        
        else:
            print('Something went wrong with the settings. Please delete the settings.json file and try again.')
        print('Action completed.')
        function.close_browser(browser, p)
except KeyboardInterrupt:
    print('Shutdown initiated, interrupt again to exit.')
    function.close_browser(browser, p)
