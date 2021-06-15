import requests
import shutil


def download_file(url):
    """
    Takes a url and downloads the file at the location. Returns the downloaded file object.

    Args:
        url: the full url to the file in format 'x/filename'.

    Returns:
        Downloaded file object

    Raises:
        None
    """
    local_filename = url.split("/")[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, "wb") as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename


# Main method.
if __name__ == "__main__":

    # [fn-1, ... ,fn-12]
    fn = "fn"
    mo = ["{:02}".format(num) for num in range(1, 13)]
    url = "https://example/com/files/"

    for m in mo:
        furl = f"{url}{fn}-{m}.csv"
        print(f"beginning - {fn}-{m}")
        fnn = download_file(furl)
        print("success - {fnn}")
