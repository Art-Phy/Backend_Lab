## Changelog

All notable changes to this project will be documented in this file.

---

### [v0.3.0] - 2026-10-03

#### Added

- Hardware Dashboard implemented in Python for external monitoring of Backend Lab.
- Real-time system metrics:
  - CPU usage.
  - RAM usage.
  - Disk usage.
  - CPU temperature.
  - System uptime.
- Infrastructure status monitoring for:
  - Nginx.
  - Docker.
  - PostgreSQL.
  - PostgreSQL backup status.
- Physical USB display integration using a Turing Smart Screen-compatible 3.5" display.
- Custom dashboard rendering using Pillow.
- Display communication adapter for the Turing Rev A protocol.
- Automatic dashboard refresh every 5 seconds.
- Dedicated Python package and executable entry point:
  - `backend-dashboard`
- Automatic startup using `backend-dashboard.service`.
- Automatic restart of the dashboard process on failure.
- Dedicated Hardware Dashboard documentation.
- Versioned systemd unit for dashboard deployment.

#### Changed

- PostgreSQL backup process now records its execution state explicitly.
- Backup status is stored in:
  - `~/.local/state/backend-lab/backup-postgresql.status`
- Hardware Dashboard now reads the explicit backup result instead of relying only on systemd service state.
- CPU temperature collection now uses the Linux thermal interface:
  - `/sys/class/thermal/thermal_zone0/temp`
- Display driver resolution now supports:
  1. Explicit driver path.
  2. `TURING_DRIVER_PATH`.
  3. Default `~/turing-smart-screen-python`.
- Main project README expanded with Hardware Dashboard architecture, monitoring capabilities and systemd integration.
- Project architecture expanded to include physical monitoring.

#### Verified

- USB display detection on Linux.
- Communication through `/dev/ttyACM0`.
- Read and write permissions using the `dialout` group.
- Successful rendering of custom frames on the physical display.
- Live CPU, RAM, disk, temperature and uptime updates.
- Correct detection of Nginx, Docker and PostgreSQL service state.
- Correct detection of successful PostgreSQL backup execution.
- Continuous dashboard updates every 5 seconds.
- Manual dashboard execution.
- Dashboard execution through systemd.
- Automatic dashboard startup after Raspberry Pi reboot.
- Automatic service restart configuration.

---

### [v0.2.0] - 2026-09-24

#### Added

- Automated PostgreSQL backup script.
- Backup generation using `pg_dump`.
- Backup validation using `pg_restore`.
- Automatic retention of the two most recent backups.
- systemd service for backup execution during controlled shutdowns and reboots.
- PostgreSQL backup and restore documentation.
- Backup-related updates to the project architecture and README.
- System timezone configured to `Europe/Madrid`.

#### Changed

- Backend Lab now follows a GitFlow-based branch structure using `main`, `develop` and `feature/*`.
- Project structure expanded to separate applications, infrastructure and backups.

#### Verified

- Manual PostgreSQL backup creation.
- Backup integrity validation.
- Successful restoration to a temporary database.
- Restored data matched the original database.
- Automatic backup execution during shutdown.
- Automatic removal of older backups beyond the two-file retention limit.

---

### [v0.1.0] - 2026-06-24

#### Added

- Initial project structure.
- Project README with architecture overview.
- Raspberry Pi setup documentation.
- SSH administration and remote access documentation.
- Docker Compose deployment documentation.
- PostgreSQL integration documentation.
- Tailscale remote access documentation.
- Maintenance and operations documentation.
- Initial project roadmap.

#### Notes

This first release establishes Backend Lab as a documented personal infrastructure project focused on backend deployment, system administration and self-hosted services using Raspberry Pi.