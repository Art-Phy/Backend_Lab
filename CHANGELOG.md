## Changelog

All notable changes to this project will be documented in this file.

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