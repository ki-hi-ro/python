import threading
import time

# ==== 改札のセンサー ====
ticket_lock = threading.Lock()  # 紙の切符スロット
suica_lock = threading.Lock()   # ICカードリーダー

# ==== Aさんが同時に2つの媒体を使って改札を通ろうとする ====
def gate_scenario():
    def use_paper_ticket():
        with ticket_lock:
            print("[A] 18きっぷを通した")
            time.sleep(1)
            print("[改札] 18きっぷを確認 → 改札通過OK")

    def suica_touched_accidentally():
        # 1秒後にSuicaが反応する（18きっぷとほぼ同時）
        time.sleep(0.5)
        # Suicaセンサーは紙の処理が完了していないときは無視する
        got_ticket = ticket_lock.acquire(timeout=1)
        if got_ticket:
            print("[改札] Suicaも反応 → しかし、紙の切符が優先されていたため無効化")
            ticket_lock.release()
        else:
            print("[改札] Suicaは反応したが、排他制御により無視された")

    print("=== 改札での排他制御の例 ===")
    t1 = threading.Thread(target=use_paper_ticket)
    t2 = threading.Thread(target=suica_touched_accidentally)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("=== 改札通過処理完了 ===")

gate_scenario()