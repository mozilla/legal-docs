from pathlib import Path
from subprocess import check_call


ROOT = Path(__file__).parent
EOL_DOCS = [
    'common_voice_challenge_terms',
    'firefox_cliqz_privacy_notice',
    'firefox_cloud_services_privacynotice',
    # 'firefox_os_privacy_notice',  # still in use in bedrock
    'firefox_screenshotgo_about_rights',
    'firefox_screenshotgo_privacy_notice',
    'fx_screenshots_privacy_notice',
    'fx_screenshots_tos',
    'firefox_testpilot_terms',
    'firefox_testpilot_privacynotice',
    'marketplace_developer_agreement',
    'marketplace_preloaded_apps_terms',
    'marketplace_privacy_policy',
    'marketplace_terms_of_use',
    'persona_privacy',
    'persona_tos',
    'webrtc_privacynotice',
    'webrtc_tos',
]


def snake_case(name):
    return name.lower().replace('-', '_')


def get_file_parts(path):
    dir_name = snake_case(path.parent.name)
    locale = path.stem
    if locale == 'en-US':
        locale = 'en'
    elif locale == 'en-US_b':
        locale = 'en_b'

    return dir_name, locale


def main():
    # clean up old directory keeping files
    for filename in ['mkdir', 'placeholder']:
        for f in ROOT.glob(f'*/.{filename}'):
            f.unlink()

    count = 0
    for mdf in ROOT.glob('*/*.md'):
        name, locale = get_file_parts(mdf)
        if name in EOL_DOCS:
            mdf.unlink()
            continue

        locale_dir = Path(locale)
        locale_dir.mkdir(exist_ok=True)
        new_mdf = locale_dir.joinpath(f'{name}.md')
        mdf.rename(new_mdf)
        count += 1
        print('.', end='', flush=True)

    # clean up empty dirs
    for name in ROOT.iterdir():
        if not name.is_dir():
            continue

        contents = list(name.iterdir())
        if not contents:
            name.rmdir()

    print(f'\nDone moving {count} files')

    # remove this file
    Path(__file__).unlink()


if __name__ == '__main__':
    main()
