# Copyright Ben Sutherland 2023. All rights reserved.

import unreal

asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()

selected_folders = unreal.MacabreEditorUtilityLibrary.get_selected_folders()
selected_assets = asset_registry.get_assets_by_paths(selected_folders, True)

if selected_assets is not None:
    num_assets = len(selected_assets)

    if num_assets > 0:
        with unreal.ScopedSlowTask(num_assets, "Reporting unused assets...") as slow_task:
            slow_task.make_dialog(True)
            for asset in selected_assets:
                if slow_task.should_cancel():
                    break
                slow_task.enter_progress_frame(1)
                package = asset.package_name

                deps = unreal.EditorAssetLibrary.find_package_referencers_for_asset(package, False)
                if len(deps) == 0:
                    print(f"{package}")
