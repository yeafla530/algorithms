for dx, dy in dirs:
    nx, ny = x + dx, y + dy
    if not in_range(nx, ny): continue
    if a[nx][ny] != 4: continue

    for teammate in teammates:
        cx, cy = teammate

        a[nx][ny], a[cx][cy] = a[cx][cy], a[nx][ny]
        nx, ny = cx, cy

        break

