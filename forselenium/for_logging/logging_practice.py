import logging
import sys

if __name__ == '__main__':
    # - 基本の使い方
    logger1 = logging.getLogger('Log1')
    logger1.addHandler(logging.StreamHandler())
    logger1.setLevel('INFO')
    logger1.info('------------')
    logger1.info('--基本のログ出力--')
    logger1.info('ただログを出力するだけならこれで良し.')
    logger1.info('------------')

    # - ログレベルの使い分け
    logger2 = logging.getLogger('Log2')
    logger2.addHandler(logging.StreamHandler())
    logger2.setLevel('INFO')
    logger2.info('------------')
    logger2.info('--ログレベルの使い分け--')
    logger2.debug('ここのログは出力されない')
    logger2.info('ログレベルをINFOに設定しておくと、')
    logger2.warning('INFO以上のログだけが出力される.')
    logger2.setLevel('DEBUG')
    logger2.debug('ログレベルを変えればDEBUGも出力される')
    logger2.info('------------')

    # - Handler
    logger3 = logging.getLogger('Log3')
    logger3.setLevel('INFO')
    logger3.info('ここは出力されない')
    hndl = logging.StreamHandler()
    logger3.addHandler(hndl)
    logger3.info('------------')
    logger3.info('--Handler--')
    logger3.info('Handlerが設定されていないとログは出力されない.')
    logger3.info('ハンドラーは取り除くこともできる.')
    logger3.removeHandler(hndl)
    logger3.info('ここは出力されない')
    logger3.addHandler(hndl)
    logger3.info('複数のHandlerを設定することもできる.')
    logger3.addHandler(logging.StreamHandler())
    logger3.info('その場合、すべてのHandlerに対して(ここだと2回)出力が行われる.')
    logger3.info('------------')

    # - StreamHandler
    logger4 = logging.getLogger('Log4')
    logger4.addHandler(logging.StreamHandler())
    logger4.setLevel('INFO')
    logger4.info('------------')
    logger4.info('--StreamHandler--')
    logger4.info('一番一般的なのが StreamHandler. コンソール上にログを出力する.')
    logger4.info('Streamを指定でき、初期値は sys.stderr になっている.')
    logger4.info('そのため、初期値のままだと赤文字でコンソール出力される.')
    logger4.removeHandler(logger4.handlers[0])
    hndl = logging.StreamHandler(stream=sys.stdout)
    logger4.addHandler(hndl)
    logger4.info('引数で sys.stdout を指定してやれば白文字で出力されるはず.')
    logger4.info('ただし出力Streamが変わるので、出力が同期されない.')
    logger4.removeHandler(logger4.handlers[0])
    logger4.addHandler(logging.StreamHandler())
    logger4.info('他に使いそうなHandlerとしてはFileHandlerとNullHandlerがある.')
    logger4.info('ふるまいは名前から想像できる通りなので詳細は割愛.')
    logger4.info('------------')

    # - format

    # - logging
    # logging.basicConfig(
    #     level='DEBUG',
    #     format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname)-8s %(message)s'
    # )

    # - logの色
