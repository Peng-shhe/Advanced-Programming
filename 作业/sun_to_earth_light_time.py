

dist_km = 149_597_870          # 地日距离（公里）
dist_m = dist_km * 1000        # 换算为米
light_speed = 299_792_458      # 光速（米/秒）

time_seconds = dist_m / light_speed
time_minutes = time_seconds / 60

print(f"地日距离: {dist_km:,} 公里")
print(f"光速: {light_speed:,} 米/秒")
print(f"光从太阳到达地球约需: {time_seconds:.2f} 秒 ≈ {time_minutes:.2f} 分钟")
