from pathlib import Path

from gilbert.content import Page
from gilbert.utils import oneshot

from webassets import Environment, Bundle


class AssetBundle(Page):
    files: list = []
    mode: str = "jsmin"

    output_extension = "js"

    @oneshot
    def env(self):
        return Environment(
            directory=self.site.dest_dir,
            load_path=[self.site.root / "assets"],
            url=str(Path(self.name).parent),
        )

    @oneshot
    def bundle(self):
        bundle = Bundle(filters=self.mode, output=str(self.output_filename), *self.files)
        return self.env.register(str(self.output_filename), bundle)

    def render(self):
        self.bundle.urls()
