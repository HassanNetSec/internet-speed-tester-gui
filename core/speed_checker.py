import speedtest

def get_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Mbps
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping
    return round(download_speed, 2), round(upload_speed, 2), round(ping, 2)
