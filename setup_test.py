# -*- coding: utf-8 -*-


if __name__ == '__main__':
    import xutil.install

    from PyQt5.QtWidgets import QApplication
    from view.video_player import VideoPlayer

    import sys

    app = QApplication(sys.argv)

    url = 'http://v.sexu.com/key=gTDWpa94BjwUYALCAlQxLA,end=1488017296,ip=79.214.77.244/sec=protect/sexu/3a/2512707-720p-x.mp4'
    url2= 'http://media.collectionofbestporn.com:8080/videos/5/8/a/6/b/58a6b3d600d8a.mp4'
    url3='http://cdn4.videos.motherlessmedia.com/videos/E5C4682.mp4?fs=opencloud'

    q_url = url3

    player = VideoPlayer(url=q_url)
    player.resize(320, 240)
    player.show()

    sys.exit(app.exec_())