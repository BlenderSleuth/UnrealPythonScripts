# Copyright Ben Sutherland 2023. All rights reserved.

import unreal

asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()

selected_folders = unreal.MacabreEditorUtilityLibrary.get_selected_folders()
selected_assets = asset_registry.get_assets_by_paths(selected_folders, True)

if selected_assets is not None:
    num_assets = len(selected_assets)

    with unreal.ScopedSlowTask(num_assets, "Reporting duplicated assets...") as slow_task:
        slow_task.make_dialog(True)
        for asset_a in selected_assets:
            if slow_task.should_cancel():
                break

            #asset_a_path = asset_a.package_path
            asset_a_full_name = asset_a.get_full_name()
            asset_a_name = asset_a.asset_name
            asset_a_class = asset_a.get_class()
            slow_task.enter_progress_frame(1, asset_a_name)

            for asset_b in selected_assets:
                asset_b_full_name = asset_b.get_full_name()
                if asset_a_full_name == asset_b_full_name:
                    break

                #asset_b_path = asset_b.package_path
                asset_b_name = asset_b.asset_name
                asset_b_class = asset_b.get_class()

                if asset_a_name == asset_b_name and asset_a_class == asset_b_class:
                    print(f">>> There is a duplicate found for the asset {asset_a_full_name} located at {asset_b_full_name}")
            