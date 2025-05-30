## Deploying Apache Airflow with Docker Compose

For official documentation, refer to the [Apache Airflow Docker Compose Setup Guide](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).

## Step 1: Download `docker-compose.yaml`

To deploy Airflow on Docker Compose, you need to fetch the official `docker-compose.yaml` file.

#### **Command (Linux/macOS):**

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/3.0.1/docker-compose.yaml'
```

#### **Command (PowerShell):**

In PowerShell, `curl` is an alias for `Invoke-WebRequest`, which does not accept the `-LfO` flags.
To use the native `curl`, explicitly call:

```powershell
curl.exe -LfO 'https://airflow.apache.org/docs/apache-airflow/3.0.1/docker-compose.yaml'
```

---

## Common Issues:

### **Issue 1:**

```plaintext
Invoke-WebRequest : A parameter cannot be found that matches parameter name 'LfO'.
```

#### **Cause:**

PowerShell's `curl` is an alias for `Invoke-WebRequest`, and it does not accept Linux-style flags like `-LfO`.

#### **Solution:**

Use the full executable call instead:

```powershell
curl.exe -LfO 'https://airflow.apache.org/docs/apache-airflow/3.0.1/docker-compose.yaml'
```

---

### **Issue 2:**

```plaintext
curl: (35) schannel: next InitializeSecurityContext failed: CRYPT_E_NO_REVOCATION_CHECK (0x80092012) - The revocation function was unable to check revocation for the certificate.
```

#### **Cause:**

This indicates a certificate revocation check failure during the SSL handshake. This is a common issue when using `curl` with Windows' default SSL backend (Schannel).

#### **Solution:**

Disable Certificate Revocation Check (Temporary Solution):

```powershell
curl.exe -LfO --ssl-no-revoke 'https://airflow.apache.org/docs/apache-airflow/3.0.1/docker-compose.yaml'
```

If you encounter further issues, consider using `Invoke-WebRequest`:

```powershell
Invoke-WebRequest 'https://airflow.apache.org/docs/apache-airflow/3.0.1/docker-compose.yaml' -OutFile 'docker-compose.yaml'
```

## Step 2: Start all services
Execute `docker compose up -d`

## Step 3: Install dependencies as `Docker Image` using `Dockerfile`
This will build image for application custom dependencies. In this repository, it is required to build custom dependency for apache-airflow package to import DAG and other modules for executing PythonOperator task.

Create requirements.txt file and add custom dependencies with required version. Utilize the file in Dockerfile for pip install
