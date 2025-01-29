from pydactyl.api import base


class MinecraftSoftware(base.PterodactylAPI):
    """Pterodactyl Client Minecraft Software API.

    Methods for interacting with the Minecraft software endpoints.
    """

    def get_minecraft_software(self, server_id):
        """Get information about available Minecraft software.

        Args:
            server_id(str): Server identifier (abbreviated UUID)

        Returns:
            dict: Response containing Minecraft software information
        """
        endpoint = f'client/servers/{server_id}/minecraft-software'
        return self._api_request(endpoint=endpoint)


class MinecraftPlayers(base.PterodactylAPI):
    """Pterodactyl Client Minecraft Player Management API.

    Methods for managing Minecraft players (whitelist, op, bans, etc).
    """

    def list_players(self, server_id):
        """Get list of players on the server.

        Args:
            server_id(str): Server identifier (abbreviated UUID)

        Returns:
            dict: Response containing player information
        """
        endpoint = f'client/servers/{server_id}/mc-players'
        return self._api_request(endpoint=endpoint)

    def set_whitelist_status(self, server_id, enabled):
        """Enable or disable the whitelist.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            enabled(bool): True to enable whitelist, False to disable

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/whitelist/status'
        data = {'enabled': enabled}
        return self._api_request(endpoint=endpoint, mode='POST', data=data)

    def add_to_whitelist(self, server_id, username):
        """Add a player to the whitelist.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            username(str): Minecraft username to whitelist

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/whitelist'
        data = {'username': username}
        return self._api_request(endpoint=endpoint, mode='PUT', data=data)

    def remove_from_whitelist(self, server_id, username):
        """Remove a player from the whitelist.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            username(str): Minecraft username to remove from whitelist

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/whitelist'
        data = {'username': username}
        return self._api_request(endpoint=endpoint, mode='DELETE', data=data)

    def op_player(self, server_id, username):
        """Give operator status to a player.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            username(str): Minecraft username to op

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/op'
        data = {'username': username}
        return self._api_request(endpoint=endpoint, mode='PUT', data=data)

    def deop_player(self, server_id, username):
        """Remove operator status from a player.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            username(str): Minecraft username to deop

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/op'
        data = {'username': username}
        return self._api_request(endpoint=endpoint, mode='DELETE', data=data)

    def ban_player(self, server_id, username, reason=None):
        """Ban a player from the server.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            username(str): Minecraft username to ban
            reason(str, optional): Reason for the ban

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/ban'
        data = {'username': username}
        if reason:
            data['reason'] = reason
        return self._api_request(endpoint=endpoint, mode='PUT', data=data)

    def unban_player(self, server_id, username):
        """Unban a player from the server.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            username(str): Minecraft username to unban

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/ban'
        data = {'username': username}
        return self._api_request(endpoint=endpoint, mode='DELETE', data=data)

    def ban_ip(self, server_id, ip, reason=None):
        """Ban an IP address from the server.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            ip(str): IP address to ban
            reason(str, optional): Reason for the ban

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/ban-ip'
        data = {'ip': ip}
        if reason:
            data['reason'] = reason
        return self._api_request(endpoint=endpoint, mode='PUT', data=data)

    def ban_ip_player(self, server_id, username, reason=None):
        """Ban a player's IP address from the server.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            username(str): Minecraft username whose IP to ban
            reason(str, optional): Reason for the ban

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/ban-ip-player'
        data = {'username': username}
        if reason:
            data['reason'] = reason
        return self._api_request(endpoint=endpoint, mode='PUT', data=data)

    def unban_ip(self, server_id, ip):
        """Unban an IP address from the server.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            ip(str): IP address to unban

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/ban-ip'
        data = {'ip': ip}
        return self._api_request(endpoint=endpoint, mode='DELETE', data=data)

    def kick_player(self, server_id, username, reason=None):
        """Kick a player from the server.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            username(str): Minecraft username to kick
            reason(str, optional): Reason for the kick

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/kick'
        data = {'username': username}
        if reason:
            data['reason'] = reason
        return self._api_request(endpoint=endpoint, mode='POST', data=data)

    def clear_inventory(self, server_id, username):
        """Clear a player's inventory.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            username(str): Minecraft username whose inventory to clear

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/clear'
        data = {'username': username}
        return self._api_request(endpoint=endpoint, mode='POST', data=data)

    def wipe_player_data(self, server_id, username):
        """Wipe all data for a player.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            username(str): Minecraft username whose data to wipe

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/wipe'
        data = {'username': username}
        return self._api_request(endpoint=endpoint, mode='POST', data=data)

    def whisper_player(self, server_id, username, message):
        """Send a private message to a player.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            username(str): Minecraft username to message
            message(str): Message to send

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/whisper'
        data = {'username': username, 'message': message}
        return self._api_request(endpoint=endpoint, mode='POST', data=data)

    def kill_player(self, server_id, username):
        """Kill a player on the server.

        Args:
            server_id(str): Server identifier (abbreviated UUID)
            username(str): Minecraft username to kill

        Returns:
            dict: Response containing operation result
        """
        endpoint = f'client/servers/{server_id}/mc-players/kill'
        data = {'username': username}
        return self._api_request(endpoint=endpoint, mode='POST', data=data) 