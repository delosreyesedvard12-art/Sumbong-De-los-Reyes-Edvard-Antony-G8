from django.db import migrations


def rename_legacy_user_tables(apps, schema_editor):
    connection = schema_editor.connection
    existing_tables = set(connection.introspection.table_names())
    table_pairs = (
        ("accounts_user", "accounts_customuser"),
        ("accounts_user_groups", "accounts_customuser_groups"),
        ("accounts_user_user_permissions", "accounts_customuser_user_permissions"),
    )

    with connection.cursor() as cursor:
        for old_table, new_table in table_pairs:
            if old_table in existing_tables and new_table not in existing_tables:
                quote = connection.ops.quote_name
                cursor.execute(
                    f"ALTER TABLE {quote(old_table)} RENAME TO {quote(new_table)}"
                )


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            rename_legacy_user_tables,
            migrations.RunPython.noop,
        ),
    ]
