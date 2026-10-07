import importlib.metadata
from .config_loader import load_config_values
from pathlib import Path
import warnings

# Edit 'config_project_template' to the appropriate repo/tool name here
__version__ = importlib.metadata.version(__package__ or "config_um_wcc") 

warnings.warn(
    "The old usage of defaulting to the IMX sensor when initializing the module is now deprecated."
    "The sensor import on common_params.toml now needs to be read in as ['sensor']['IMX'] or ['sensor']['HWK']."
    "The sensor name can be set in ['sensor']['sensor_name'] parameter in the toml.",
    DeprecationWarning
)

def get_data_path():
    package_root = Path(__file__).parent.resolve()
    data_path = package_root / "support_data"

    if not data_path.exists():
        raise FileNotFoundError(f"Support data directory not found: {data_path}")

    return str(data_path)

__all__ = ["load_config_values", "get_data_path", "__version__"]