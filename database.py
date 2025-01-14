import psycopg2
from psycopg2.extras import RealDictCursor

class Database:
    def __init__(self, db_url):
        self.connection = psycopg2.connect(db_url, cursor_factory=RealDictCursor)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS gpu_metrics (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT NOW(),
            temperature INT,
            gpu_utilization INT,
            power_draw FLOAT
        );
        CREATE TABLE IF NOT EXISTS optimization_logs (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT NOW(),
            target_performance INT,
            power_limit INT,
            suggestion FLOAT
        );
        """)
        self.connection.commit()

    def insert_metric(self, temperature, gpu_utilization, power_draw):
        self.cursor.execute("""
        INSERT INTO gpu_metrics (temperature, gpu_utilization, power_draw)
        VALUES (%s, %s, %s);
        """, (temperature, gpu_utilization, power_draw))
        self.connection.commit()

    def insert_optimization_log(self, target_performance, power_limit, suggestion):
        self.cursor.execute("""
        INSERT INTO optimization_logs (target_performance, power_limit, suggestion)
        VALUES (%s, %s, %s);
        """, (target_performance, power_limit, suggestion))
        self.connection.commit()

    def fetch_metrics(self):
        self.cursor.execute("SELECT * FROM gpu_metrics ORDER BY timestamp DESC LIMIT 10;")
        return self.cursor.fetchall()

if __name__ == "__main__":
    db = Database("postgresql://user:password@localhost/nevida_ai")
    db.create_tables()
