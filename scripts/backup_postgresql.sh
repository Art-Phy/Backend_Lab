
#!/usr/b9in/env bash


set -euo pipefail


BACKUP_DIR="$HOME/backups/postgresql"
CONTAINER_NAME="url-shortener-postgres"
DB_NAME="url_shortener"
DB_USER="arturo_api"
MAX_BACKUP=2

TIMESTAMP="$(date +%Y-%m-%d_%H-%M-%S)"
BACKUP_FILE="${BACKUP_DIR}/${DB_NAME}_${TIMESTAMP}.dump"

mkdir -p "$BACKUP_DIR"

echo "[INFO] Starting PostgreSQL backup..."

docker exec "$CONTAINER_NAME" \
    pg_dump \
    -U "$DB_USER" \
    -d "$DB_NAME" \
    -Fc \
    > "$BACKUP_FILE"

if [[ ! -s "$BACKUP_FILE " ]]; then
    echo "[ERROR] Backup file is empty."
    rm -f "$BACKUP_FILE"
    exit 1
fi

docker exec -i "$CONTAINER_NAME" \
    pg_restore -l \
    < "$BACKUP_FILE" \
    > /dev/null

echo "[INFO] Backup created successfully:"
echo "       $BACKUP_FILE"

mapfile -t BACKUPS < <(
    find "$BACKUP_DIR" \
        -maxdepth 1 \
        -type f \
        -name "${DB_NAME}_*.dump" \
        -printf '%T@ %p\n' \
        | sort -nr \
        | cut -d ' ' -f2-
 )

 if (( ${#BACKUPS[@]} > MAX_BACKUPS )); then
    for OLD_BACKUP in "${BACKUPS[@]:MAX_BACKUPS}"; do
        echo "[INFO] Removing old backup: $OLD_BACKUP"
        rm -f -- "$OLD_BACKUP"
    done
fi

echo "[INFO] Backup process completed"
